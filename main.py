import requests

def main():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    print(response.text)

    # update foo

if __name__ == '__main__':
    main()