floaters = [1.2, 3.5, 4.8, 9.2]

for assignment in floaters:
    print(assignment)

big_list = list(range(33,100))

for num in big_list:
    #check for odd number
    if num % 2 != 0:
        print(num, end = " ")