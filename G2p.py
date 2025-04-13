ARABIC_ONES = {
    0: "",1: "واحد",2: "اثنان",3: "ثلاثة",4: "أربعة",5: "خمسة",6: "ستة",7: "سبعة",8: "ثمانية",9: "تسعة",10: "عشرة",
    11: "أحد عشر",12: "اثنا عشر",13: "ثلاثة عشر",14: "أربعة عشر",15: "خمسة عشر",16: "ستة عشر",17: "سبعة عشر",
    18: "ثمانية عشر",19: "تسعة عشر"
}

ARABIC_TENS = {
    0: "",10: "عشرة", 20: "عشرون",30: "ثلاثون",40: "أربعون",50: "خمسون",60: "ستون",70: "سبعون",80: "ثمانون",90: "تسعون"
}


dic_trans = {
    'أ': 'Ɂ', 'ب': 'b', 'ت': 't', 'ث': 'θ', 'ج': 'ʒ', 'ح': 'ħ', 'خ': 'x', 'د': 'd', 'ذ': 'ð', 'ر': 'r', 'ز': 'z',
    'س': 's', 'ش': 'ʃ', 'ص': 'sˁ', 'ض': 'dˁ', 'ط': 'tˁ', 'ظ': 'ðˁ', 'ع': 'ʕ', 'غ': 'ɣ', 'ف': 'f', 'ق': 'q', 'ك': 'k',
    'ل': 'l', 'م': 'm', 'ن': 'n', 'ه': 'h', 'ة': 'h', 'و': 'w', 'ي': 'j', 'َ': 'a', 'ِ': 'i', 'ُ': 'u', 'ا': 'aː', 'ى': 'æ',
    'ئ': 'Ɂ', 'آ': 'A', 'إ': 'ʡI', 'ء': 'ʡ', 'ؤ': 'uʡ'
}

text = input('Enter text: ')
text.split()

# Handling specific cases for normalization
if text.startswith('ال') and text[2] not in dic_trans:
    text = text.replace(text[1], text[2])
if text.endswith('وا'):
    text = text.replace('وا', 'u:')

# Normalize diacritics
for char in range(len(text) - 1):
    if text[char] == "ِ" and text[char + 1] == 'ي':
        text = text.replace("ِي", "i:")
    elif text[char] == "ُ" and text[char + 1] == 'و':
        text = text.replace("ُو", "u:")

# Remove symbols and normalize the text
symbols_to_remove = "@#,$^&*()!~"
modified_text = ""
for char in text:
    if   char == '%':
        modified_text += ' فِي المِئة '  # Replacing the percentage
    elif char == '$':
        modified_text += 'دُولار ' # replacing the dollar sign
    elif char == '.':
        modified_text += ' pause' # making pause
    elif char not in symbols_to_remove:
        modified_text += char # removing unwanted sympols and returns the new normal text

# Convert numbers to words in Arabic
tokens = modified_text.split() # splitiing the normalized text
converted_numbers = []         # making an empty list for converting numbers to words and adding the word in it 

for token in tokens:
    try:
        number = int(token) # it will take and convert only the numbers in the input 

        if number in ARABIC_ONES: 
            converted_numbers.append(ARABIC_ONES[number])   # If the number is found in ARABIC_ONES, it means the number is from 1 to 19, 
                                                            # and we directly append the corresponding word to the converted_numbers list.
        
        else:                                               # If the number is not found in ARABIC_ONES, it means the number is 20 or greater. In this case, we calculate the tens and ones separately
            tens = (number // 10) * 10                      # tens represents the nearest multiple of 10 less than or equal to the given number.    يعني الرقم الي داخل الاول هيقسمة بالفلور علشان يشوف الفئة بعدها هيضربة *10 علشان الفئة تنتمي للعشرات                 
            ones = number % 10                              # ones represents the remaining value after subtracting the tens. هنا هيجبلي الارقام الي باقيه لو فيه 
            if ones == 0:
                converted_numbers.append(ARABIC_TENS[tens]) # If the remaining ones is equal 0, it means the number is a multiple of 10, and we append the word for the tens directly to the converted_numbers list.
            else:
                converted_numbers.append(ARABIC_ONES[ones]+ " و " + ARABIC_TENS[tens] ) 
                                                            # If the remaining ones is not equal 0, we append both the word for the tens and the word for the ones, separated by "و" .
    except ValueError:
        converted_numbers.append(token)                     # if ther's any number it will avoid the error and append the text to converted numbers

final_text = ' '.join(converted_numbers)                    # we will link the converted numbers which includes our text also to new variable 

# Transliterate using the provided dictionary
table = final_text.maketrans(dic_trans)                     # Trannslating our text to phonemes
transliterated_text = final_text.translate(table) 

print(transliterated_text)
