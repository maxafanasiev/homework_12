import os
import oop


address_book = oop.AddressBook()
bot_working = True
clear = lambda: os.system('clear')


def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except UnboundLocalError:
            print('Enter command')
            return func(*args,**kwargs)
        except TypeError:
            print('Enter name and phone separated by a space!')
            return func(*args,**kwargs)
        except KeyError:
            print('This name not found!')
            return func(*args,**kwargs)
        except IndexError:
            print('This name found! Enter another name.')
            return func(*args,**kwargs)
        except ValueError:
            return func(*args,**kwargs)
    return(inner)


def start():
    clear()
    address_book.load_from_file("address_book.json")
    print("CLI Address book bot is running...")
    print("Address book loaded.")


def show_page(page_number=1, count=5):
    clear()
    return address_book.show_page(page_number, count)


def helper():
    clear()
    res = ''
    for key in COMMANDS.keys():
        res += f"{key}\n"
    return "Available bot function:\n" + res


def close():
    clear()
    global bot_working
    bot_working = False
    address_book.save_to_file('address_book.json')
    return ("Good bye!\n Bot stopped.")


def hello():
    clear()
    return ('How can I help you?')


@input_error
def add_record(name, phone='' ,birthday=''):
    clear()
    rec_name = oop.Name()
    rec_name.value = name

    rec_phone = oop.Phone()
    rec_phone.value = phone

    rec_bd = oop.Birthday()
    rec_bd.value = birthday

    rec = oop.Record(rec_name, rec_phone, rec_bd)

    address_book.addRecord(rec)
    return rec.print_record()


def change_phone(name, old_phone, new_phone):
    clear()
    rec = address_book[name]
    o_ph = oop.Phone()
    o_ph.value = old_phone
    n_ph = oop.Phone()
    n_ph.value = new_phone
    rec.change_phone(o_ph, n_ph)
    return rec.print_record()


def add_phone(name, phone):
    clear()
    rec = address_book[name]
    ph = oop.Phone()
    ph.value = phone
    rec.add_phone(ph)
    return rec.print_record()


def add_birthday(name, birthday):
    clear()
    rec = address_book[name]
    bd = oop.Birthday()
    bd.value = birthday
    rec.add_birthday(bd)
    return rec.print_record()


def delete_phone(name, phone):
    clear()
    rec = address_book[name]
    ph = oop.Phone()
    ph.value = phone
    rec.del_phone(ph)
    return rec.print_record()


def days_to_birthday(name):
    clear()
    rec = address_book[name]
    return rec.days_to_birthday()


def showall():
    clear()
    return address_book.print_all()



def phone(name):
    clear()
    rec = address_book[name]
    return rec.print_record()


def unknown_command():
    return "Unknown command, try again"


def command_parse(s):
    for key, cmd in  COMMANDS.items():
        if key in s.lower():
            return cmd, s[len(key):].strip().split()
    return unknown_command, []


COMMANDS = {'hello':hello,
            'days to bd':days_to_birthday,
            'add phone': add_phone,
            'add birthday': add_birthday,
            'change phone':change_phone,
            'delete phone': delete_phone,
            'find phone':phone,
            'show page':show_page,
            'show all':showall,
            'good bye':close,
            'exit':close,
            'close':close,
            'add': add_record,
            'help':helper,
            }


@input_error
def main():
    start()
    while bot_working:
        s = input()
        command, arguments = command_parse(s)
        print(command(*arguments))


if __name__ == '__main__':
    clear()
    main()