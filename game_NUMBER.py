import random

def guess_number():
    print("🎮 Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать!")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Введи своё число: "))
            attempts += 1
            
            if guess < secret_number:
                print("📈 Загаданное число БОЛЬШЕ!")
            elif guess > secret_number:
                print("📉 Загаданное число МЕНЬШЕ!")
            else:
                print(f"\n🎉 Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
                break
                
        except ValueError:
            print("⚠️ Пожалуйста, введи целое число!")

if __name__ == "__main__":
    guess_number()