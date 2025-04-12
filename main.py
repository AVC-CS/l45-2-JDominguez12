import random


def main():
    total = 0
    numbers = []
    previous_num = 0
    while True:
        num = random.randint(1, 10)
        if total > 100:
            total = total - previous_num
            break
        else:
            total = total + num
            previous_num = num
            numbers.append(num)

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
