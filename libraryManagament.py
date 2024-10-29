
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Kitap kaydetme fonksiyonu
def save_book():
    # Girdi alanlarındaki verileri al
    title = title_entry.get()
    author = author_entry.get()
    publisher = publisher_entry.get()
    quantity = quantity_entry.get()
    notes = notes_entry.get()

    # Boş alan kontrolü
    if not title or not author or not publisher or not quantity:
        messagebox.showwarning("Input Error", "Please fill out all required fields.")
        return

    # Kitap bilgilerini txt dosyasına kaydet
    with open("books.txt", "a") as file:
        file.write(f"{title},{author},{publisher},{quantity},{notes}\n")
    
    # Kullanıcıya başarı mesajı göster ve alanları temizle
    messagebox.showinfo("Success", "Book saved successfully!")
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    publisher_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    notes_entry.delete(0, tk.END)

# Kitapları listeleme fonksiyonu
def list_books():
    try:
        # Kitapları gösteren alanı temizle
        result_text.delete(1.0, tk.END)
        
        # Dosyadaki kitapları okuma
        with open("books.txt", "r") as file:
            books = file.readlines()
            
            # Her bir kitabı listeye ekleme
            if books:
                result_text.insert(tk.END, "List of Books:\n\n")
                for book in books:
                    result_text.insert(tk.END, book)
            else:
                result_text.insert(tk.END, "No books found.\n")
    
    except FileNotFoundError:
        result_text.insert(tk.END, "No books file found.\n")

# GUI kurulum
root = tk.Tk()
root.title("Library Management")

# Kitap Adı
tk.Label(root, text="Book Title:").grid(row=0, column=0, padx=10, pady=5)
title_entry = tk.Entry(root, width=30)
title_entry.grid(row=0, column=1, padx=10, pady=5)

# Yazar
tk.Label(root, text="Author:").grid(row=1, column=0, padx=10, pady=5)
author_entry = tk.Entry(root, width=30)
author_entry.grid(row=1, column=1, padx=10, pady=5)

# Yayın Evi
tk.Label(root, text="Publisher:").grid(row=2, column=0, padx=10, pady=5)
publisher_entry = tk.Entry(root, width=30)
publisher_entry.grid(row=2, column=1, padx=10, pady=5)

# Adet
tk.Label(root, text="Quantity:").grid(row=3, column=0, padx=10, pady=5)
quantity_entry = tk.Entry(root, width=30)
quantity_entry.grid(row=3, column=1, padx=10, pady=5)

# Ek Notlar
tk.Label(root, text="Notes:").grid(row=4, column=0, padx=10, pady=5)
notes_entry = tk.Entry(root, width=30)
notes_entry.grid(row=4, column=1, padx=10, pady=5)

# Kaydet Butonu
save_button = tk.Button(root, text="Save Book", command=save_book)
save_button.grid(row=5, column=0, pady=10)

# Listeleme Butonu
list_button = tk.Button(root, text="List Books", command=list_books)
list_button.grid(row=5, column=1, pady=10)

# Kitapları gösteren kaydırılabilir metin kutusu
result_text = scrolledtext.ScrolledText(root, width=60, height=15)
result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
