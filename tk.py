from random import *
from tkinter import *
import math

size_x = 700
size_y = 700
triangle_line_width = 600
deep_level = 10

root = Tk()
root.title('Serpinsky triangle')
canvas = Canvas(root, width=size_x, height=size_y, bg="white")
canvas.pack()


f_point = [size_x / 2 - triangle_line_width / 2, size_y / 2 - (triangle_line_width * math.sqrt(3)) / 6]
s_point = [size_x / 2, size_y / 2 + (triangle_line_width * math.sqrt(3)) / 3]
t_point = [size_x / 2 + triangle_line_width / 2, size_y / 2 - (triangle_line_width * math.sqrt(3)) / 6]

def draw_polygon(x1, y1, x2, y2, x3, y3, t_line_width, level):
	if level == deep_level:
		return

	point_1 = [x1 + t_line_width / 4, y1 + (t_line_width / 2) * math.sqrt(3) / 2]
	point_2 = [(x3 - x1) / 2 + x1, y1]
	point_3 = [x3 - t_line_width / 4, y3 + (t_line_width / 2) * math.sqrt(3) / 2]	
	canvas.create_polygon((point_1[0], size_y - point_1[1], point_2[0], size_y - point_2[1], point_3[0], size_y - point_3[1]), fill="white", outline="black")
	draw_polygon(x1, y1, point_1[0], point_1[1], point_2[0], point_2[1], t_line_width / 2, level + 1)
	draw_polygon(point_1[0], point_1[1], x2, y2, point_3[0], point_3[1], t_line_width / 2, level + 1)
	draw_polygon(point_2[0], point_2[1], point_3[0], point_3[1], x3, y3, t_line_width / 2, level + 1)

canvas.create_polygon((f_point[0], size_y - f_point[1], s_point[0], size_y - s_point[1], t_point[0], size_y - t_point[1]), fill="black")
draw_polygon(f_point[0], f_point[1], s_point[0], s_point[1], t_point[0], t_point[1], triangle_line_width, 1)

mainloop()





