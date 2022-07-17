# Ініцілізовано функцію, напишіть в тілі функції логіку яка
# перетворить вхідну строчку за певною логікою.

# Функція приймає на вхід будь яку строчку і виводить в консоль за допомогою функції print()
#  оновлену версію цієї строчки.
# Якщо довжина строчки більша ніж 5 символів -> Потрібно вивести лише перші 5 символів та в кінці додати три точки (...).
# Якщо перша літера строчки U або u (регістр не важливий) -> Вивести всю строчку в Upper Case (верхній регістр)
# Якщо перша літера строчки L або l (регістр не важливий) -> Вивести всю строчку в Lower Case (нижній регістр)
# Якщо жодна умова вище не підходить - вивести строку без змін.
# Декілька умов можуть пересікатись!
# Можна додавати свої тести за прикладом. Потрібно врахувати обробку можливих помилок.

# Наприклад:
#   transformStr('Testing string') - > 'Testi...' (довжина більше 5 символів)
#   transformStr('Lux') - > 'lux' (Починается на L)
#   transformStr('up') - > 'UP' (Починается на U)
#   transformStr('Luxery') - > 'luxer...' (Починается на L + довжина більше 5 символів)


def transformStr(str):
    """if  len(str) > 5:
        print(str[:5] + '...')
    if str[0] in ['l','L'] : 
        print(str.lower())   
    if str[0] in ['u','U'] :
        print(str.upper())"""
    
    """print(str[:5] + '...') if len(str) > 5 else print(str)  
    if str[0] in ['l','L'] : 
        print(str.lower())   
    elif str[0] in ['u','U'] :
        print(str.upper()) """   

    if  len(str) < 5:
        if str[0] == 'L' or str[0] == 'l':
           print(str.lower())
        elif str[0] == 'U' or str[0] =='u':
           print(str.upper())
        else:
            print(str)   
    elif len(str) > 5:  
        if str[0] == 'L' or str[0] == 'l':
           print(str[:5].lower() + '...')
        elif str[0] == 'U' or str[0] =='u':
           print(str[:5].upper() + '...')
        else:
            print(str[:5] + '...')

transformStr('Testing string') # 'Testi...' (довжина більше 5 символів)
transformStr('Lux') # 'lux' (Починается на L)
transformStr('up') # 'UP' (Починается на U)
transformStr('Luxery') # 'luxer...' (Починается на L + довжина більше 5 символів)
transformStr('Test')