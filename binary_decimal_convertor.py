print("Type 'bd' for binary to decimal conversion")
print("Type 'db' for decimal to binary conversion")
user_input = input()

if user_input == 'bd':
    print('Enter the binary number you want to convert')
    binary_input = input()
    binary_list = list(binary_input)
    result = 0
    binary_length = len(binary_list)
    while binary_length> 0:
        for i in binary_list:
            result = result + (int(i) * (2**(binary_length - 1)))
            binary_length -= 1
    print(f"{result} is the decimal conversion of {binary_input}")
elif user_input == 'db':
    print('convertor under construction')
else:
    print("Give a valid input from 'db' or 'bd'")