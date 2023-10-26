# Author Michael Vasconcelos

import decoder

# Adds pswd by three and goes back to ones place when needed
def encode(password):
    encoded_pswd = ''
    for i in password:
        encoded = int(i)
        encoded += 3
        if encoded <= 9:
            encoded = str(encoded)
        elif encoded > 9:
            encoded %= 10
            encoded = str(encoded)
        encoded_pswd += encoded
    return encoded_pswd


def main():
    option = 0
    encoded_pswd = ''
    while option != 3:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit')
        option = int(input('Please enter an option'))
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_pswd = encode(password)
            print('Your password has been encoded and stored!')
        elif option == '2':
            decoded_pswd = decoder.decode(encoded_pswd)
            print(f"The encoded password is {encoded_pswd},",
                  f"and the original password is {decoded_pswd}")
        elif option == '3':
            quit()
        else:
            print('Invalid Option')
            continue


if __name__ == '__main__':
    main()