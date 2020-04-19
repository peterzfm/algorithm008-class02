def plusOne(digits):
    str_digits=''.join(str(digit) for digit in digits )
    int_digits= int(str_digits)+1
    str_digits=str(int_digits)
    list_str_digits=list(str_digits)
    digits=[int(digit) for digit in list_str_digits]
    return digits

digits=[1,2,3]
print(plusOne(digits))

