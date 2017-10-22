dic = { 0: [(' ', '-', ' '), ('|', ' ', '|'), (' ', ' ', ' '), ('|', ' ', '|'), (' ', '-', ' ')], 
		1: [(' ', ' ', ' '), (' ', ' ', '|'), (' ', ' ', ' '), (' ', ' ', '|'), (' ', ' ', ' ')],    
		2: [(' ', '-', ' '), (' ', ' ', '|'), (' ', '-', ' '), ('|', ' ', ' '), (' ', '-', ' ')],    
		3: [(' ', '-', ' '), (' ', ' ', '|'), (' ', '-', ' '), (' ', ' ', '|'), (' ', '-', ' ')],    
		4: [(' ', ' ', ' '), ('|', ' ', '|'), (' ', '-', ' '), (' ', ' ', '|'), (' ', ' ', ' ')],    
		5: [(' ', '-', ' '), ('|', ' ', ' '), (' ', '-', ' '), (' ', ' ', '|'), (' ', '-', ' ')],    
		6: [(' ', '-', ' '), ('|', ' ', ' '), (' ', '-', ' '), ('|', ' ', '|'), (' ', '-', ' ')],    
		7: [(' ', '-', ' '), (' ', ' ', '|'), (' ', ' ', ' '), (' ', ' ', '|'), (' ', ' ', ' ')],    
		8: [(' ', '-', ' '), ('|', ' ', '|'), (' ', '-', ' '), ('|', ' ', '|'), (' ', '-', ' ')],    
		9: [(' ', '-', ' '), ('|', ' ', '|'), (' ', '-', ' '), (' ', ' ', '|'), (' ', '-', ' ')] }

def run():
    print 'The 7 segments display.\n'
    size = input('Enter the size of the display: ')
    inputNumbers = input('Enter the numbers that you want display (comma separated: 1,2,3): ')
    numbers = [inputNumbers] if isinstance(inputNumbers, int) else [int(c) for c in inputNumbers]

    display(mapped_numbers(numbers), size)

def mapped_numbers(numbers):
	return [dic[number] for number in numbers]

def my_print(s):
	print s,

def display(mapped, size):
	top       = [d[0][0] + d[0][1] * size + d[0][2] for d in mapped]
	midtop    = [d[1][0] + d[1][1] * size + d[1][2] for d in mapped]
	mid       = [d[2][0] + d[2][1] * size + d[2][2] for d in mapped]
	midbotton = [d[3][0] + d[3][1] * size + d[3][2] for d in mapped]
	botton    = [d[4][0] + d[4][1] * size + d[4][2] for d in mapped]

	map(my_print, top)
	print

	for x in range(size):
		map(my_print, midtop)
		print

	map(my_print, mid)
	print

	for x in range(size):
		map(my_print, midbotton)
		print

	map(my_print, botton)
	print

run()