import random

def age_guessing_game():
    print("=== 나이 맞추기 게임을 시작합니다 ===")
    print("컴퓨터가 생각한 나이를 맞춰보세요 (1부터 100까지)")
   
    # 컴퓨터가 생각하는 나이를 랜덤하게 선택
    computer_age = random.randint(1, 100)
   
    while True:
        try:
            user_guess = int(input("추측한 나이를 입력하세요: "))
           
            if user_guess < 1 or user_guess > 100:
                print("1부터 100 사이의 숫자를 입력해주세요.")
                continue
           
            if user_guess < computer_age:
                print("더 큰 나이를 추측해보세요.")
            elif user_guess > computer_age:
                print("더 작은 나이를 추측해보세요.")
            else:
                print(f"축하합니다! 컴퓨터가 생각한 나이는 {computer_age}세입니다!")
                break
       
        except ValueError:
            print("유효한 숫자를 입력해주세요.")

if __name__ == "__main__":
    age_guessing_game()
