# test_script.py
def my_function(name):
    print(f"Hello, {name} from a GitHub Action!")
    return f"Processed: {name}"

if __name__ == "__main__":
    result = my_function("Bot")
    print(result)