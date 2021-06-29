import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

HOST = '127.0.0.1'
PORT = 5005

class Client:
	
	def __init__(self, host, port):

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((host, port))

		msg = tkinter.Tk()
		msg.withdraw()

		self.nickname = simpledialog.askstring("Nickname", "Please Choose a nickname", parent=msg)

		self.gui_done = False 
		self.running = True

		gui_thread = threading.Thread(target=self.gui_loop)
		receive_thread = threading.Thread(target=self.receive)

		gui_thread.start()
		receive_thread.start()

	def gui_loop(self):
		self.win = tkinter.Tk()
		self.win.configure(bg="lightblue")

		self.chat_label = tkinter.Label(self.win, text = (self.nickname+" - Chat Windows"), bg="lightblue")
		self.chat_label.config(font=("Arial", 14))
		self.chat_label.pack(padx=25, pady=5) #padding

		self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
		self.text_area.pack(padx=25, pady=5)
		self.text_area.config(state='disabled') #supaya gabisa ngerubah2 isi chat history

		self.msg_label = tkinter.Label(self.win, text="Input Message:", bg="lightblue")
		self.msg_label.config(font=("Arial", 14))
		self.msg_label.pack(padx=25, pady=5)

		self.input_area = tkinter.Text(self.win, height=5)
		self.input_area.pack(padx=20, pady=5)

		self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
		self.send_button.config(font=("Arial", 14))
		self.send_button.pack(padx=25, pady=5)

		self.gui_done = True

		self.win.protocol("WM_DELETE_WINDOW", self.stop)

		self.win.title("Tubes SISTER - Chat Application 		*User: "+self.nickname+"*")

		self.win.mainloop()


#run
client = Client(HOST,PORT)