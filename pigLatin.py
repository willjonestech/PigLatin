def translate(str):

    # Set variable to hold pig latin expression
    pig_latin = ''
    # Set variable to hold vowels (instead of using regex)
    vowels = 'aeiou'
    # Check if the first character is a vowel
    if str[0].lower() in vowels:
        pig_latin = str + 'way'
        return pig_latin

    else: # Else find first vowel occurence
        for char in str:
            if char in vowels:
                # Set index of first vowel occurence
                vowelIndex = str.index(char)
                break

        # Combine expressions
        pig_latin = str[vowelIndex:] + str[:vowelIndex] + 'ay'
        return pig_latin

print(translate('World'))
