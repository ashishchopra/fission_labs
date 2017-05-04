def sort_on_all(a):
    return sorted(a, key=lambda ele: (ele[0], int(ele[1]), int(ele[2])))


input_list = []

message = 'Give input eg. Tom,19,80. Hit enter twice when done! : '
print(message)
while True:
    try:
        x, y, z = input().split(',')
        input_list.append((x, y, z))
    except Exception as e:
        break

# a = [('Tom', 19, 80), ('John', 20, 90),
#     ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85)]

sorted_list = sort_on_all(input_list)
print(sorted_list)
