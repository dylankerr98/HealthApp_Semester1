def main():
    print('Welcome to the Nutrition reporting program.\n')  # Welcome user to program.

    print('Below is a list of actions this program can carry out.\n')

    print('#1 - Display current number of stored records on account.\n' +
          '#2 - Display list of foods & details.\n' +
          '#3 - Count total calories for all records currently stored.\n' +
          '#4 - Calculate average serving weight on number of records currently stored.\n' +
          '#5 - Add a new food record to list and re-sort based on time.\n' +
          '#6 - Display number of items for each food type.\n' +
          '#7 - Display all records which are over,sat fat threshold.\n' +
          '#8 - Quit program.\n')

    print('Please enter number of action you would like to preform.')

    action = 1

    while action != 8:

        try:

            action = int(input('\nPreform action: '))

            if action == 1:

                print("1")

            elif action == 2:

                print("2")

            elif action == 3:

                print("3")

            elif action == 4:

                print("4")

            elif action == 5:

                print("5")

            elif action == 6:

                print("6")

            elif action == 7:

                print("7")

            else:

                while action < 1 or action > 8:

                    if action == 1:

                        print("1")

                    elif action == 2:

                        print("2")

                    elif action == 3:

                        print("3")

                    elif action == 4:

                        print("4")

                    elif action == 5:

                        print("5")

                    elif action == 6:

                        print("6")

                    elif action == 7:

                        print("7")

            print('\n---------------------------')

        except ValueError:

            print('\nError, not a valid response, must be number.')


def open_file_read():
    all_records = open('Food items.txt', 'r')

    return all_records


def open_file_append():
    all_records = open('Food items.txt', 'a')

    return all_records


def open_file_write():
    all_records = open('Food items.txt', 'w')

    return all_records


def close_file(all_records):
    all_records.close()


def create_list(all_records):
    food_record_list = []

    for row in all_records:

        if not row.startswith('#'):
            row = row.rstrip('\n').split(', ')

            food_record_list.append(row)

    return food_record_list


def count_records(all_records):
    line_count = 0

    with all_records:
        for _ in all_records:
            line_count += 1

        print('\nThere are currently', line_count - 2, 'food records' +
              ' stored on this account.')


def print_records(all_records):
    print('\nTIME    MEAL TYPE    DESCRIPTION    SERVING    KCAL    SFATg\n')

    for single_record in all_records:

        if not single_record.startswith('#'):
            print(single_record)


def cnt_total_kcal(food_record_list):
    total_cal = 0

    for item in range(len(food_record_list)):
        total_cal += float(food_record_list[item][4])

    print('\nThe total calorie count for all records is: ', format(total_cal, '.2f'))


def cal_average_serving(food_record_list):
    total_cal = 0

    for item in range(len(food_record_list)):
        total_cal += float(food_record_list[item][3])

    print('\nThe average serving amount is: ', format(total_cal / len(food_record_list), '.2f'))


def add_new_record(all_records):
    try:

        print('\nPlease enter the details for the new record below.')

        time = str(input('Time: '))
        meal_type = str(input('Meal type: '))
        description = str(input('Description: '))
        serving = int(input('Serving: '))
        kcal = int(input('KCAL: '))
        sfatg = float(input('SFATg: '))

        all_records.write(('\n' + time) + ', ')
        all_records.write(meal_type + ', ')
        all_records.write(description + ', ')
        all_records.write(str(serving) + ', ')
        all_records.write(str(kcal) + ', ')
        all_records.write(str(sfatg))

    except ValueError:

        print('Sorry, wrong data type entered.')


def sum_record_type(food_record_list):
    breakfast = 0
    snack = 0
    lunch = 0
    dinner = 0

    for item in range(len(food_record_list)):

        if food_record_list[item][1] == 'Breakfast':

            breakfast += 1

        elif food_record_list[item][1] == 'Snack':

            snack += 1

        elif food_record_list[item][1] == 'Lunch':

            lunch += 1

        elif food_record_list[item][1] == 'Dinner':

            dinner += 1

    print('\nThe total number of food items in each category are:\n')
    print('Breakfast: ', breakfast)
    print('Snack: ', snack)
    print('Lunch: ', lunch)
    print('Dinner: ', dinner)


def over_sfat_thres(food_record_list):
    threshold = float(input('\nPlease enter the saturated fat threshold to return records: '))

    print('\nTIME' + '\t' + 'MEAL TYPE' + '\t' + 'DESCRIPTION' + '\t' + 'SERVING' + '\t' + 'KCAL' + '\t' + 'SFATg\n')

    for item in range(len(food_record_list)):

        if float(food_record_list[item][5]) > threshold:
            print(food_record_list[item][0] + '\t', food_record_list[item][1] + '\t', food_record_list[item][2] + '\t',
                  food_record_list[item][3] + '\t', food_record_list[item][4] + '\t', food_record_list[item][5])


main()
