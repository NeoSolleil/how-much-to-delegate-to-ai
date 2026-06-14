from datetime import date


def calculate_age(birthday: date, today: date) -> int:
    """誕生日と今日の日付から満年齢を返す。"""
    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1
    return age


if __name__ == "__main__":
    # 一見ちゃんと動いているように見えるケース
    print(calculate_age(date(1990, 3, 15), date(2026, 6, 11)))  # 36（正しい）

    # 誕生日が「今月のこれから来る日」のとき
    print(calculate_age(date(1990, 6, 20), date(2026, 6, 11)))  # 36 と出るが、正しくは 35
