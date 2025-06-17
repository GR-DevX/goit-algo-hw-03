import argparse
import shutil
from pathlib import Path

def parse_arguments():
    """Парсить аргументи командного рядка."""
    parser = argparse.ArgumentParser(description="Рекурсивно копіює та сортує файли за розширенням.")
    parser.add_argument("source_dir", type=Path, help="Шлях до вихідної директорії.")
    parser.add_argument("dest_dir", type=Path, nargs='?', default=Path("dist"), \
                        help="Шлях до директорії призначення (за замовчуванням 'dist').")
    return parser.parse_args()

def copy_and_sort_files(source_path: Path, dest_path: Path):
    """
    Рекурсивно обробляє директорії та копіює файли, сортуючи їх за розширенням.

    Args:
        source_path (Path): Поточний шлях у вихідній директорії.
        dest_path (Path): Шлях до базової директорії призначення.
    """
    try:
        for item in source_path.iterdir(): # Перебираємо всі елементи у директорії [cite: 12]
            if item.is_dir():
                # Рекурсивний виклик для піддиректорії [cite: 12]
                # Файли з піддиректорій також сортуються у головну директорію призначення
                copy_and_sort_files(item, dest_path)
            elif item.is_file(): # Якщо елемент є файлом, він має бути доступним для копіювання [cite: 13]
                file_extension = item.suffix[1:]  # Отримуємо розширення без крапки (e.g., 'txt', 'jpg')
                if not file_extension: # Файли без розширення
                    file_extension = "no_extension"

                # Створюємо піддиректорію для розширення у директорії призначення [cite: 14]
                extension_dir = dest_path / file_extension
                extension_dir.mkdir(parents=True, exist_ok=True)

                # Копіюємо файл [cite: 14]
                shutil.copy2(item, extension_dir / item.name)
                print(f"Скопійовано: {item} -> {extension_dir / item.name}")

    except FileNotFoundError:
        print(f"Помилка: Директорію {source_path} не знайдено.")
    except PermissionError:
        print(f"Помилка: Немає доступу до {source_path} або його вмісту.")
    except Exception as e:
        print(f"Виникла непередбачувана помилка при обробці {source_path}: {e}")

def main():
    args = parse_arguments()
    source_directory = args.source_dir
    destination_directory = args.dest_dir

    print(f"Вихідна директорія: {source_directory}")
    print(f"Директорія призначення: {destination_directory}")

    if not source_directory.exists() or not source_directory.is_dir():
        print(f"Помилка: Вихідна директорія '{source_directory}' не існує або не є директорією.")
        return

    try:
        destination_directory.mkdir(parents=True, exist_ok=True) # Створюємо директорію призначення, якщо її немає
        copy_and_sort_files(source_directory, destination_directory)
        print("Копіювання та сортування завершено.")
    except Exception as e:
        print(f"Загальна помилка під час виконання: {e}") # Обробка винятків [cite: 15]

if __name__ == "__main__":
    main()
