import fitz  # PyMuPDF

# Открываем исходный PDF файл
input_pdf_path = "text.pdf"
pdf_document = fitz.open(input_pdf_path)

# Список слов для выделения
# Функция для чтения слов из TXT файла
def load_words_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        words = [line.split()[0] for line in file.readlines()]
    return words

# Загрузка списка слов для выделения из TXT файла
words_txt_path = "1.txt"
words_to_highlight = load_words_from_txt(words_txt_path)
print(words_to_highlight)
# Функция для выделения слов в документе
def highlight_words(pdf_document, words_to_highlight):
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        for word in words_to_highlight:
            text_instances = page.search_for(word)
            for inst in text_instances:
                highlight = page.add_highlight_annot(inst)
                highlight.update()
            words_to_highlight

# Выделяем слова
highlight_words(pdf_document, words_to_highlight)

# Сохраняем измененный PDF
output_pdf_path = "highlighted_text.pdf"
pdf_document.save(output_pdf_path)

output_pdf_path