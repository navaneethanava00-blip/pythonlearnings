import threading

def display():
    for i in range(5):
        print("Hello")


t1 = threading.Thread(target=display)

t1.start()


print("Main Thread")
