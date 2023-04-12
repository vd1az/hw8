from datetime import datetime, timedelta, date

users = [
    {'name': 'Alice', 'birthday': datetime(1990, 4, 1)},
    {'name': 'Bob', 'birthday': datetime(1985, 3, 15)},
    {'name': 'Charlie', 'birthday': datetime(1995, 4, 18)},
    {'name': 'David', 'birthday': datetime(1992, 3, 16)},
    {'name': 'Eve', 'birthday': datetime(1998, 3, 18)}
]

def get_birthdays_per_week(users):
    today = date.today()
    current_year = today.year
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)
    
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  # noqa: E501
    
    birthdays = {}
    for user in users:
        name = user['name']
        bday = user['birthday'].replace(year=current_year).date()
        if bday >= monday and bday <= sunday:
            weekday = weekdays[bday.weekday()]
            if weekday not in birthdays:
                birthdays[weekday] = []
            birthdays[weekday].append(name)
            
    for weekday, names in birthdays.items():
        print(f"{weekday}: {', '.join(names)}")
        
if __name__ == "__main__":
    get_birthdays_per_week(users)