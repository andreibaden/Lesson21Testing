import view
import logic

# controller
def main():
    while True:
        size = int(input("Input size of list: "))
        if size > 0:
            break
        else:
            view.write("Error. User data was invalid.")

    ls = create_list(size)

    rnd_init_list(ls)
    user_init_list(ls)

    second = logic.find_second_max_value(ls)

    msg = f"Second max value is {second}."

    view.write(msg)



if __name__ == "__main__":
    main()