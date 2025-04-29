class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Current queue:", self.items)

def menu():
    customer_queue = Queue()
    
    while True:
        print("\nMenu:")
        print("1. Tambah queue")
        print("2. Hapus queue")
        print("3. Cek isi queue")
        print("4. Tampilkan queue")
        print("5. Keluar")
        
        option = input("Masukkan opsi (1-5): ")
        
        if option == '1':
            item = input("Masukkan nama pelanggan untuk ditambahkan ke queue: ")
            customer_queue.enqueue(item)
            print(f"Pelanggan {item} telah ditambahkan ke queue.")
        
        elif option == '2':
            try:
                customer = customer_queue.dequeue()
                print(f"Pelanggan {customer} telah dihapus dari queue.")
            except IndexError as e:
                print(e)
        
        elif option == '3':
            if customer_queue.is_empty():
                print("Queue saat ini kosong.")
            else:
                print(f"Isi queue: {customer_queue.items}")
        
        elif option == '4':
            customer_queue.display()
        
        elif option == '5':
            print("Keluar dari program.")
            break
        
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

menu()