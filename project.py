alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift):
    if direction == "encode":
        cipher_text = ""
        for letter in text:
            if letter in alphabets:
                index = alphabets.index(letter)
                new_index = (index + shift) % len(alphabets)  # Use modulo for wrap-around
                cipher_text += alphabets[new_index]
            else:
                cipher_text += letter  # Non-alphabet characters remain unchanged
        print(f"The encoded text is : {cipher_text}")

    elif direction == "decode":
        plain_text = ""
        for letter in text:
            if letter in alphabets:
                position = alphabets.index(letter)
                new_position = (position - shift) % len(alphabets)  # Use modulo for wrap-around
                plain_text += alphabets[new_position]
            else:
                plain_text += letter  # Non-alphabet characters remain unchanged
        print(f"The decoded text is : {plain_text}")
continue_or_not=True
while continue_or_not:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift)
    ask=input("Type 'yes' if you want to continue. Otherwise type 'no'\n").lower()
    if ask=="no":
        continue_or_not=False
        print("Good Bye!")