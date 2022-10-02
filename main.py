def id_check(id_list):
    if len(id_list) != 9:
        return False

    id_check_list = []
    x = 0
    for num in id_list:
        if x % 2 != 0:
            new_num = num * 2
            if new_num > 9:
                num_list = [int(num) for num in str(new_num)]
                new_num = sum(num_list)
            id_check_list.append(new_num)
        else:
            id_check_list.append(num)
        x += 1

    if sum(id_check_list) % 10 != 0:
        return False
    return True


def id_calc(id_number):
    id_list = [int(num) for num in str(id_number)]
    if not id_check(id_list):
        print("The id you entered is invalid!")
        return False

    id_sum = sum(id_list)
    multiplication = 1
    for num in id_list:
        multiplication *= num

    id_modulo = id_sum % 10

    print(f"\nId status: Valid!\nNumbers of id: {', '.join([str(num) for num in id_list])}\nSum of numbers: {id_sum}\n"
          f"Multiplication of numbers {multiplication}\nModulo of numbers: {id_modulo}")


number = int(input("Enter your id number: "))
id_calc(id_number=number)
