def handle_numbers(number1, number2, number3):
    count = 0
    for i in range(number1, number2+1):
        if i % number3 == 0:
            count+=1
    return count
