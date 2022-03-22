

def intro():
    ticker0 = 0
    ticker1 = 0
    ticker2 = 0
    sum_dict = {}
    begin_string = 'Before we begin, some students like to find the sum of certain numbers\n'
    example = 'EX:  If you want to know the sum of many HW assignments, you can input them here and get the sum\n'
    answer = input(f'{begin_string}{example}Is this something you need to do? y/n ')
    if answer == 'y' or answer == 'Y':
        q1 = int(input('How many TOTAL sums do you need to calculate?: '))
        list_arrays = [[] for _ in range(q1)]
        for i in range(q1):
            ticker0 += 1
            values = int(input(f'How many values would you like to add to sum {ticker0}: '))
            for v in range(values):
                ticker1 += 1
                num = float(input(f'VALUE {ticker1} = '))
                list_arrays[i].append(num)
        for i in range(q1):
            ticker2 += 1
            sum_dict[f'SUM {ticker2}'] = sum(list_arrays[i])
        print("your sums are as follows:")
        print(sum_dict)
    else:
        pass