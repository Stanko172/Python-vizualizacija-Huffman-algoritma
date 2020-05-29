import tkinter as tk
from tkinter import *
import heapq
import os

HEIGHT = 650
WIDTH = 1200

class Node:
    def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, Node)):
            return False
        return self.freq == other.freq


class HeapHuffman:
	def __init__(self):
		self.heap = []
		self.process = ""

	def find_freq(self, text):
		freq = {}
		for ch in text:
			if not ch in freq:
				freq[ch] = 0
			freq[ch] += 1
		return freq

	def construct_heap(self, freq):
		for key in freq:
			node = Node(key, freq[key])
			heapq.heappush(self.heap, node)

			self.process += "Stvoren član f(%s)\n" % (node.freq)

	def merge_nodes(self):
		while(len(self.heap)>1):
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)

			self.process += "Spajanje članova f(%s) i f(%s)\n" % (node1.freq, node2.freq)

			merged = Node(str(node1.freq + node2.freq), node1.freq + node2.freq)
			merged.left = node1
			merged.right = node2

			self.process += "Stvoren novi član f(%s)\n" % (merged.freq)

			heapq.heappush(self.heap, merged)


def check_left_nodes(node):
    obj = node
    left_array = []
    right_array = []

    counter = 0
    
    while obj.left != None:
        left_array.append(obj.left.char)
        if obj.right != None and counter >= 1:
            right_array.append(obj.right.char)
        else:
            right_array.append(None)
                
        obj = obj.left
        counter += 1

    return left_array, right_array

def check_right_nodes(node):
    obj = node
    right_array = []
    left_array = []

    counter = 0

    while obj.right != None:
        if obj.right != None:
            right_array.append(obj.right.char)
            if obj.left != None and counter >= 1:
                left_array.append(obj.left.char)
            else:
                left_array.append(None)

        obj = obj.right
        counter += 1

    return right_array, left_array

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

def make_canvas(nodes_list):
    x = 300
    for node in nodes_list:
        left_nodes = None
        right_nodes = None
        
        y = 90
        r = 25
        
        canvas.create_circle(x, y, r, fill="white", outline="blue", width=4)
        canvas.create_text(x,y,text=node.char)
        canvas.update()

        #Lijeva strana čvora
        if node.left != None:
            left_nodes = check_left_nodes(node)

            if len(left_nodes[0]) > 0:
                node_obj = None
                node_obj = None
                x2 = x
                y2 = y

                xr2 = x
                yr2 = y
                for i in range(len(left_nodes[0])):
                    node_obj = left_nodes[0][i]
                    canvas.create_line(x2, y2 + 20, x2 - 50, y2 + 90)

                    canvas.create_circle(x2 - 50, y2 + 90, 25, fill="white", outline="blue", width=4)
                    canvas.create_text(x2 - 50,y2 + 90,text=node_obj)
                    canvas.update()

                    node_obj_right = left_nodes[1][i]
                    if node_obj_right != None:
                        canvas.create_line(x2 + 20, y2 + 20, x2 + 50, y2 + 90)

                        canvas.create_circle(x2 + 50, y2 + 90, 25, fill="white", outline="blue", width=4)
                        canvas.create_text(x2 + 50,y2 + 90,text=node_obj_right)
                        canvas.update()

                    x2 = x2 - 60
                    y2 += 90

            #desna strana čvora
            if node.right != None:
                right_nodes = check_right_nodes(node)

                if len(right_nodes[0]) > 0:
                    node_obj = None

                    xr2 = x
                    yr2 = y

                    for i in range(len(right_nodes[0])):
                        node_obj = right_nodes[0][i]

                        canvas.create_line(xr2, yr2 + 20, xr2 + 150, yr2 + 90)

                        canvas.create_circle(xr2 + 150, yr2 + 90, 25, fill="white", outline="blue", width=4)
                        canvas.create_text(xr2 + 150,yr2 + 90,text=node_obj)
                        canvas.update()

                        node_obj_left = right_nodes[1][i]
                        if node_obj_left != None:
                            canvas.create_line(xr2 - 25, yr2 + 35, xr2 - 50, yr2 + 90)

                            canvas.create_circle(xr2 - 50, yr2 + 90, 25, fill="white", outline="blue", width=4)
                            canvas.create_text(xr2 - 50,yr2 + 90,text=node_obj_left)
                            canvas.update()
                        
                        xr2 += 170
                        yr2 += 80
                        
                
                    
            
        #print(left_nodes)
        
        x += 280

def make_object(entry):
    huffman_object = HeapHuffman()

    print(huffman_object.find_freq(entry))

    freq_dict = huffman_object.find_freq(entry)
    huffman_object.construct_heap(freq_dict)

    huffman_object.merge_nodes()

    max_node = huffman_object.heap[0]
    nodes_list = [max_node]

    #print(huffman_object.process)
    
    make_canvas(nodes_list)

    text.insert(INSERT, huffman_object.process)
    


def build_tree(entry):
    make_object(entry)

def clear_canvas():
    canvas.delete('all')
    text.delete('1.0', END)

top_frame = tk.Frame(root, bg="#1f4386", bd=10)
top_frame.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.09)

label = tk.Label(top_frame,text="Huffman Coding", font=( 'Berlin Sans FB', 18),bg="#1f4386", fg="white")
label.place(relwidth=0.3, relheight=1)

    
lower_frame = tk.Frame(root, bg="#1f4386", bd=10)
lower_frame.place(relx=0.0, rely=0.65, relwidth=0.7, relheight=0.6)

#Side frame
side_frame = tk.Frame(root, bg="white", bd=10)
side_frame.place(relx=0.7, rely=0.09, relwidth=0.3, relheight=1.0)

build_button = Button(side_frame, text="Build tree", fg="#1f4386", command= lambda: build_tree(entry.get()))
build_button.pack( side = RIGHT, anchor="ne" )

clear_button = Button(side_frame, text="Reset", fg="#1f4386", command= lambda: clear_canvas())
clear_button.pack( side = RIGHT, anchor="ne" )

entry = tk.Entry(side_frame, bg="lightgrey", font=40)
entry.pack()

text = Text(side_frame)
text.pack()

tk.mainloop()
