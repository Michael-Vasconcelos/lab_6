# Author: Paul Baroco


# shift digits of numeric string back 3, wrapping when needed
def decode(password: str) -> str:
    return ''.join(
        [chr((ord(c) - ord('0') - 3) % 10 + ord('0')) for c in password]
    )
