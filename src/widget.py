from src.masks import get_mask_card_number


def mask_account_card(string: str) -> tuple[str, str]:
    """ Функция маскировки цифр карты и счета """
    string_split = string.split()
    name_card_or_score = " ".join(string_split[:2])
    number_card_or_score = string_split[-1]

    return name_card_or_score, number_card_or_score

test = "Visa Platinum 7000792289606361"
name_card, card_number = mask_account_card(test)

masked_number = get_mask_card_number(card_number)
print(f"{name_card}: {masked_number}")


def get_date(data: str) -> str:
    data_1 = data[:10]
    data_2 = data_1.split('-')
    if data_2[::-1]:
        return f"{data_2[2]}.{data_2[1]}.{data_2[0]}"
    return ''

print(get_date("2024-03-11T02:26:18.671407"))