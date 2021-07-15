# Dictionary with alphabet as keys and its correspondents in morse_code
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..',
                   'E': '.', 'F': '..-.',
                   'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.',
                   'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-',
                   'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---',
                   '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..',
                   '9': '----.', '0': '-----'}

# Create a while loop to prompt the user for a string to be translated
while True:
    text = input("Type the text to be translated to morse code:\n").upper()

    # Create a for loop to translate characters to morse code without breaking a new line at the end
    for char in text:
        if char == ' ':
            print('  ', end='')
        elif char in MORSE_CODE_DICT:
            print(f'{MORSE_CODE_DICT[char]} ', end='')

    # Printing a new line before a new prompt to user
    print('')

    # Prompt the user to know if he wants to continue to translate strings
    wanna_play = input('Type "y" if you want to try translate another text.\n').lower()

    # Condition to break the loop if user do not want to continue translating
    if wanna_play != 'y':
        break
