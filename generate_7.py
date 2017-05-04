class Genarate7(object):
    """Generates numbers divisible by 7
    betwwen range 0 and n"""
    def __init__(self, n, i=0):
        self.i = i
        self.n = n

    def __iter__(self):
        i = self.i
        while i < self.n:
            if i % 7 == 0:
                yield i
            i += 1


n = int(input('Enter the value of n. : '))
g7 = Genarate7(n, 0)

for i in g7:
    print(i)
