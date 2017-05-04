import sys
import math


class Robot(object):
    """Reperesents Robot that moves
    Up, Down, Left and Right."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, steps):
        self.y += steps

    def move_down(self, steps):
        self.y -= steps

    def move_right(self, steps):
        self.x += steps

    def move_left(self, steps):
        self.x -= steps

    def find_dist(self, init_x, init_y):
        sq_sum = ((self.x - init_x) ** 2) + ((self.y - init_y) ** 2)
        return int(round(math.sqrt(sq_sum)))


robot = Robot(0, 0)

# instruction_list = [
#     ('UP', 5),
#     ('DOWN', 3),
#     ('LEFT', 3),
#     ('RIGHT', 2)
# ]

instruction_list = []
message = 'Give input eg. DOWN 3. Hit enter twice when done! : '
print(message)
while True:
    try:
        direction, steps = input().split(' ')
        instruction_list.append((direction, int(steps)))
    except Exception as e:
        break

for direction, steps in instruction_list:
    if direction == 'UP':
        robot.move_up(steps)
    elif direction == 'DOWN':
        robot.move_down(steps)
    elif direction == 'RIGHT':
        robot.move_right(steps)
    elif direction == 'LEFT':
        robot.move_left(steps)
    else:
        print('Unsupported direction!')
        sys.exit()

dist = robot.find_dist(0, 0)
print(dist)
