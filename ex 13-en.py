name = []
day = []
place = []
food = []
choice = 'Y'

while (choice == 'Y'):
    name.append(input('\nName: '))
    day.append(input('Which day do you prefer? Saturday (S) or Sunday (D): '))
    place.append(input('Which place do you prefer? Beach (B) or Club (C): '))
    food.append(input('Which food do you prefer? Barbecue (B) or snacks (S): '))
    choice = input('Do you want to enter a new answer? [Y/N] ')
    
saturday = [i for i in range(len(day)) if day[i] == 'S' or day[i] == 's']
sunday = [i for i in range(len(day)) if day[i] == 'D' or day[i] == 'd']
beach = [i for i in range(len(place)) if place[i] == 'B' or place[i] == 'b']
club = [i for i in range(len(place)) if place[i] == 'C' or place[i] == 'c']
barbecue = [i for i in range(len(food)) if food[i] == 'B' or food[i] == 'b']
snack = [i for i in range(len(food)) if food[i] == 'S' or food[i] == 's']

if (len(saturday) > len(sunday)):
    print(f'\nSaturday was the chosen day!')
    for index in saturday:
        print(f'The people who voted were: {name[index]}')
else:
    print('The party will be on Sunday.')
    for index in sunday:
        print(f'\nThe people who voted were: {name[index]}')

if (len(beach) > len(club)):
    print('The party will be on the beach.')
    for index in beach:
        print(f'The people who voted were: {name[index]}')
else:
    print('The party will be at the club.')
    for index in club :
        print(f'The people who voted were: {name[index]}')

if (len(barbecue) > len(snack)):
    print('We are going to eat barbecue.')
    for index in barbecue:
        print(f'The people who voted were: {name[index]}')
else:
    print('We are going to eat snacks.')
    for index in snack:
        print(f'The people who voted were: {name[index]}')
