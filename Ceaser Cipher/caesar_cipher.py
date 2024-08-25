import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount = -shift_amount

    for letter in original_text:
        if letter.lower() not in alphabet:
            output_text += letter
        else:
            is_upper = letter.isupper()
            letter = letter.lower()
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            new_letter = alphabet[shifted_position]
            if is_upper:
                new_letter = new_letter.upper()
            output_text += new_letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ['encode', 'decode']:
        print("Invalid choice. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n")
    shift = input("Type the shift number:\n")
    
    if not shift.isdigit():
        print("Please enter a valid number for the shift.")
        continue
    
    shift = int(shift)
    
    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
