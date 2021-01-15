import random
import pickle

class Sudoku():
	def menu(self):
		pass

	def load_file(self):
		pass
		
	def save_file(self):
		pass

	def choose_side(self):
		"""
		Функция позволяет игроку определить 
		на какой стороне играть.
		"""
		answer = int(input('\nВведите 0/1 соответствующий игровому режиму'))

		while answer not in range(0, 2):
			print('Error: введите корректный ответ')
			answer = int(input('\nВведите 0/1 соответствующий игровому режиму'))

		if answer == 1:
			print('Отлично! Вы играете за себя! Удачи.')
			side = 1
		elif answer == 0:
			print('Отлично! За Вас будет играть Ваша стратегия!')
			side = 0

	def print_rules(self):
		"""
		Данная функция выводит правила игры.
		"""
		print("""
			Добро пожаловать в консольную игру – Судоку!
			В данной игре Вам придется решить Судоку – головоломку с числами на доске 9х9\n
			Правила довольно просты:
				1. Сперва, Вам придется выбрать сторону, за которую Вы хотите играть:
					1. Введите 0 – если хотите играть за компьютер, суть заключается в том, что
					Вам придется задать игровое поле и, затем, компьютер попытается
					решить задачу или сообщит о невозможности ее решения;\n
					2. Введите 1 - если хотите играть за себя. В данном режим реализованы правила
					стандартного судоку на доске 9x9, вкратце:
					Имеем квадратную доску, поделенную на 9 квадратов 3х3.
					В начале игры, случайным образом, в некоторые ячейки ставятся числа от 1 до 9
					От игрока требуется заполнить пустые ячейки числами от 1 до 9 таким образом,
					чтобы введенная цифра встречалась только один раз в соответствующем квадрате 3х3,
					строке и столбце. 
					В общем случае - каждая цифра встречается только один раз в кажом столбце,
					кажой строке, каждом квадрате 3х3.\n
				2. Ввести количество заполненных ячеек, тем самым Вы можете определить для
				себя сложность игры: чем больше заполненных изначально ячеек - тем проще игра.\n
				3. Затем, в зависимости от выбранной стороны, Вам придется вводить определенные
				комманды вида: (Строка, Колонка, Число) или ожидать конца работы алгоритма. \n 
			Удачной игры!
			""")

	def start_grid(self):
		"""
		Функция позволяет задать стартовое расположение чисел
		на доске. В ней использутся функции randomize(grid) и
		check_cell(rand_grid, num_fill_cells)
		grid – формирование изначальной доски
		rand_grid – доска со случайно перемешанными числами
		start_grid – итоговая доска, в которой удалено опред. число ячеек
		"""
		num_fill_cells = int(input('Введите количество заполненных ячеек(от 1 до 80): '))
		if num_fill_cells not in range(1, 81):
			error = True
			print('Ошибка! Введено некорректное число заполненных строк.')
			pass
		else:
			n = 3
			grid = [[int((i*n + i/n + j) % (n*n) + 1) for j in range(n*n)] for i in range(n*n)]
			rand_grid = self.randomize(grid)
			start_grid = self.check_cell(rand_grid, num_fill_cells)

		return start_grid

	def swap_rows(self, grid):
		"""
		функция производит смену строк в рамках одной секции,
		состоящей из 3-х строк
		Берется центральная строка одной секции,
		таким образом, i = {1,4,7}
		"""
		i = random.randrange(1, 10, 3)
		rand_grid = grid[i]
		choice = random.randint(0,1)
		if choice == 0:
			grid[i], grid[i-1] = grid[i-1], grid[i]
		else:
			grid[i], grid[i+1] = grid[i+1], grid[i]

		return grid

	def swap_cols(self, grid):
		"""
		функция производит перемешивание колонок:
		на первом шаге транспонируем доску и 
		кладем результат в переменную var
		затем производим смену строк функцией
		swap_rows()
		наконец, повторно транспонируем, тем 
		самым приводим строки и столбцы на свои места,
		поменяв при этом некоторые два столбца исходной доски
		"""
		var = list(map(list, zip(*grid)))
		grid1 = self.swap_rows(var)
		grid2 = list(map(list, zip(*grid1)))

		return grid2

	def swap_all_rows(self, grid):
		pass

	def swap_all_cols(self, grid):
		pass

	def randomize(self, grid):
		"""
		функция применяет 9 случайных элементарных
		преобразований из имеющихся
		func - случайная функция из списка имеющихся
		grid - применение преобхования к доске
		"""
		functions = [self.swap_cols, self.swap_rows]


		for _ in range(1, 10):
			func = random.randrange(0, len(functions))
			grid = functions[func](grid) # self.funcs[]()


		return grid

	def check_cell(self, nums, num_fill_cells):
		"""
		функция выдает в результате доску с 
		некоторым количеством заполненных
		ячеек, указанных игроком
		"""
		check = 0
		num_unfill = 81 - num_fill_cells

		while check < num_unfill:
			row = random.randint(0,8)
			col = random.randint(0,8)
			if nums[row][col] == 0:
				check = check
			else:
				nums[row][col] = '*'
			check += 1

		return nums

	def display_grid(self, grid):
		"""
		функция графически отображает текущую доску
		"""
		s = grid
		print(f"""
     0   1   2   3   4   5   6   7   8
    –––––––––––––––––––––––––––––––––––
  0| {s[0][0]} | {s[0][1]} | {s[0][2]} | {s[0][3]} | {s[0][4]} | {s[0][5]} | {s[0][6]} | {s[0][7]} | {s[0][8]} |
   |–––––––––––|–––––––––––|–––––––––––|
  1| {s[1][0]} | {s[1][1]} | {s[1][2]} | {s[1][3]} | {s[1][4]} | {s[1][5]} | {s[1][6]} | {s[1][7]} | {s[1][8]} |
   |–––––––––––|–––––––––––|–––––––––––|
  2| {s[2][0]} | {s[2][1]} | {s[2][2]} | {s[2][3]} | {s[2][4]} | {s[2][5]} | {s[2][6]} | {s[2][7]} | {s[2][8]} |
    ––––––––––––––––––––––––––––––––––– 
  3| {s[3][0]} | {s[3][1]} | {s[3][2]} | {s[3][3]} | {s[3][4]} | {s[3][5]} | {s[3][6]} | {s[3][7]} | {s[3][8]} |
   |–––––––––––|–––––––––––|–––––––––––
  4| {s[4][0]} | {s[4][1]} | {s[4][2]} | {s[4][3]} | {s[4][4]} | {s[4][5]} | {s[4][6]} | {s[4][7]} | {s[4][8]} |
   |–––––––––––|–––––––––––|–––––––––––|
  5| {s[5][0]} | {s[5][1]} | {s[5][2]} | {s[5][3]} | {s[5][4]} | {s[5][5]} | {s[5][6]} | {s[5][7]} | {s[5][8]} |
    –––––––––––––––––––––––––––––––––––
  6| {s[6][0]} | {s[6][1]} | {s[6][2]} | {s[6][3]} | {s[6][4]} | {s[6][5]} | {s[6][6]} | {s[6][7]} | {s[6][8]} |
   |–––––––––––|–––––––––––|–––––––––––|
  7| {s[7][0]} | {s[7][1]} | {s[7][2]} | {s[7][3]} | {s[7][4]} | {s[7][5]} | {s[7][6]} | {s[7][7]} | {s[7][8]} |
   |–––––––––––|–––––––––––|–––––––––––|
  8| {s[8][0]} | {s[8][1]} | {s[8][2]} | {s[8][3]} | {s[8][4]} | {s[8][5]} | {s[8][6]} | {s[8][7]} | {s[8][8]} |
    ––––––––––––––––––––––––––––––––––– 
  """)

	def player_mode(self, side):
		"""
		функция определяет режим игры: для игрока иначе pass
		"""
		if side == 0:
			pass
		else:
			self.player_play()

	def player_play(self):
		"""
		функция описывет функционал игрока
		основная игра – описана в цикле while
		после выхода из него игра считается выигранной игроком/сохранненной
		в итоге выводится либо функция поздравления с победой
		либо функция позволяющая продолжить ранее сохраненную игру
		"""
		grid = self.start_grid()
		print("\nНачнем игру!\n")
		self.display_grid(grid)
		
		while not self.winner(grid):
			row = int(input("Введите номер строчки: "))
			print()
			col = int(input("Введите номер столбца: "))
			print()
			num = int(input("Введите значение от 1 до 9: "))
			if (grid[row][col] == '*') and (num in range(1, 10)):
				grid = self.if_uniq(grid, row, col, num)
			else:
				print('\nОшибка! Данная ячейка уже занята!\n')
				continue

		if not self.save_file():
			self.congrats_for_p()
		else:
			self.menu()

	def if_uniq(self, grid, row, col, num):
		trans_grid = list(map(list, zip(*grid)))
		if (num not in grid[row]) and (num not in trans_grid[col]):
			grid[row][col] = num
			self.display_grid(grid)
			return grid
		else:
			print("\nОшибка! Введено неверное значение!")
			return grid

	def winner(self, grid): 
		for i in range(len(grid)):
			for j in range(len(grid)):
				if grid[i][j] == '*':
					return False

		return True

	def congrats_for_p(self):
		print(f"""\n\tПоздравляю, Ты решил судоку!
			Если хочешь играть на более сложном уровне,
			запусти игру еще раз, но выбери меньшее количество заполненных ячеек.
			Хочешь опробовать то, решить ли компьютер твою задачу?
			Запусти игру в режиме для компьютера. 
			Спасибо за то, что играл! Удачи!""")
	
	def comp_mode(self, side):
		if side == 1:
			pass
		else:
			grid = self.start_grid()
			comp_play(grid)

	def comp_play(self, grid):
		pass

	def valid(self):
		pass

	def find_empty(self, grid):
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if grid[i][j] == 0:
					return (i, j)

		return None

	def congrats_for_algo(self):
		pass

	def lose_algo(self):
		pass

	def main(self):
		self.menu()
		self.print_rules()
		self.choose_side()
		self.comp_mode(side)
		self.player_mode(side)


game = Sudoku()
game.main()
