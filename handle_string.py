def handle_string(value):
    symbols = ['!','@','#','$','%',',','.','?']
    for symbol in symbols:
        if symbol in value:
            value = value.replace(symbol,'')
    value = value.replace(' ', '')
    num = [int(i) for i in value if i.isdigit()]
    count_numbers = len(num)
    count_letters = len(value) - count_numbers
    result = ("Letters - {} \nDigits - {}".format(count_letters, count_numbers))
    return result


    
        
