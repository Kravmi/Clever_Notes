#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QListWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QLabel, QInputDialog, QMessageBox
import json

with open('f.json', 'r') as file:
    data = json.load(file)

def show_note():
    text_note = list_notes.selectedItems()[0].text()
    text_field.setText(data[text_note]['текст'])
    list_tags.clear()
    list_tags.addItems(data[text_note]['теги'])

def add_note():
    name_note, result = QInputDialog.getText(main_win, "Добавить заметку", 'Название заметки')
    if name_note != '' and result == True:
        data[name_note] = {'текст' : '', 'теги' : []}
        list_notes.addItem(name_note)
        list_tags.addItems(data[name_note]['теги'])

def del_note():
    if list_notes.selectedItems():
        text_note = list_notes.selectedItems()[0].text()
        del data[text_note]
        text_field.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(data)
        with open('f.json', 'w') as file:
            json.dump(data, file, ensure_ascii = False)
    else:
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Ошибка")
        msg_box.setText("Вы не выбрали заметку!")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

def save_note():
    if list_notes.selectedItems():
       text_note = list_notes.selectedItems()[0].text()
       data[text_note]['текст']
       text_field.toPlainText()
       with open('f.json', 'w') as file:
           json.dump(data, file, ensure_ascii = False)

app = QApplication([])
main_win = QWidget()
main_win.resize(900, 600)
main_win.setWindowTitle('Умные заметки')
layout_v_1 = QVBoxLayout()
text_field = QTextEdit()
layout_v_1.addWidget(text_field, alignment=Qt.AlignLeft)
layout_v_2 = QVBoxLayout()
list_notes_label = QLabel('Список заметок')
layout_v_2.addWidget(list_notes_label)
list_notes = QListWidget()
layout_v_2.addWidget(list_notes)
list_notes.addItems(data)
layout_h = QHBoxLayout()
layout_h_1 = QHBoxLayout()
layout_h_2 = QHBoxLayout()
layout_h_3 = QHBoxLayout()
layout_h_4 = QHBoxLayout()
button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')
layout_h_1.addWidget(button_note_create)
layout_h_1.addWidget(button_note_del)
layout_h_2.addWidget(button_note_save)
layout_v_2.addLayout(layout_h_1)
layout_v_2.addLayout(layout_h_2)
layout_h.addLayout(layout_v_1)
layout_h.addLayout(layout_v_2)
list_tags_label = QLabel('Список тегов')
layout_v_2.addWidget(list_tags_label)
list_tags = QListWidget()
layout_v_2.addWidget(list_tags)
tag_text = QLineEdit()
tag_text.setPlaceholderText('Введите тег...')
layout_v_2.addWidget(tag_text)
button_add_to_note = QPushButton("Добавить к заметке")
button_separate_to_note = QPushButton("Открепить от заметки")
button_search_note = QPushButton('Искать заметки по тегу')
layout_h_3.addWidget(button_add_to_note)
layout_h_3.addWidget(button_separate_to_note)
layout_h_4.addWidget(button_search_note)
layout_v_2.addLayout(layout_h_3)
layout_v_2.addLayout(layout_h_4)
list_notes.itemClicked.connect(show_note)
button_note_create.clicked.connect(add_note)
button_note_del.clicked.connect(del_note)
button_note_save.clicked.connect(save_note)
main_win.setLayout(layout_h)
main_win.show()
app.exec_()