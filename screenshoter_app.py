import pyscreenshot
# Capture the full screen
print("="*151)
print("Enoch Screenshoter😉")
print("="*151)
while True:
    choice = input("Do you want to screenshot your screen(yes/no): ").lower().strip()
    if choice =="yes":
        image = pyscreenshot.grab()
        view = input ("do you wanna view it (yes/no): ").lower().strip()
        if view == "yes":
            # Display the screenshot
            image.show()
            saver_image = input("do you want to save your screenshot(yes/no): ").lower().strip()
            if saver_image == "yes":
                # Save the screenshot to a file
                image_name = input("save file as: ")
                image.save(f"{image_name}.png")
                print(f"Your screenfeshot saved as {image_name}.png ✅✅")
            elif saver_image == "no":
                print("image not saved❌❌")
                exit()
            else :
                print("invalid operation, try again!!")
        elif view == "no":
            saver_image = input("do you want to save your screenshot(yes/no): ").lower().strip()
            if saver_image == "yes":
                # Save the screenshot to a file
                while True:
                    try:
                        image_name = input("save file as: ").strip()
                        if not image_name:
                            raise ValueError
                    except Exception:
                        print("INVALID FILENAME❌❌")
                        continue
                    image.save(f"{image_name}.png")
                    print(f"Your screenshot saved as {image_name}.png ✅✅")
                    exit()
            
            elif saver_image == "no":
                print("image not saved❌❌")
                print("Exiting program❌❌")
                exit()

            else :
                print("invalid operation, try again!!")
                
        else:
            print("invalid input , insert 'yes/no'")
    elif choice== "no":
        leave = input ("do you wanna exit this program(yes/no): ").lower().strip()
        if leave== "yes":
            print("thanks for using Enoch screenshoter, byeeeeee!!!")
            exit()
        elif leave == "no":
            print("Fine , then answer me 🤨🙄")
        else :
            print("Invalid input , try again!!")
    else:
        print("Invalid input , try again!(yes/no)🕛")