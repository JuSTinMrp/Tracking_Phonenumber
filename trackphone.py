import phonenumbers
from phonenumbers import geocoder
ph_num1 = phonenumbers.parse("+919629403033")
# ph_num2 = phonenumbers.parse("")
# ph_num3 = phonenumbers.parse("")
# ph_num4 = phonenumbers.parse("")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(ph_num1,"en"))
# print(geocoder.description_for_number(ph_num2,"en"))
# print(geocoder.description_for_number(ph_num3,"en"))
# print(geocoder.description_for_number(ph_num4,"en"))
