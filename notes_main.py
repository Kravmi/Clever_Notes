from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QPushButton, QApplication, QWidget,
                             QListWidget, QVBoxLayout, QHBoxLayout,
                             QTextEdit, QLineEdit, QLabel, QInputDialog)
import os

notes = list()

note = []
files = os.listdir('Zametki')
for file in files:
    print(file)
    with open('Zametki/' + file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.replace('\n', '')
            note.append(line)
    info = note[0].split('|')
    note[0] = info[0]
    note.insert(1, info[1])
    try:
        tags = note[3].split()
    except IndexError:
        tags = []
    note[3] = tags
    notes.append(note)
    print(note)
    note = []


def show_note():
    text_note = list_notes.selectedItems()[0].text()
    for note in notes:
        if text_note == note[0]:
            text_field.setText(note[2])
            list_tags.clear()
            list_tags.addItems(note[3])


def add_note():
    name_note, result = QInputDialog.getText(
        main_win, "Добавить заметку", 'Название заметки')
    if name_note != '' and result:
        filename = str(len(notes) + 1) + '.txt'
        note = [name_note, str(len(notes) + 1), '', []]
        notes.append(note)
        list_notes.addItem(note[0])
        print(note)
        print(notes)
        with open('Zametki/' + filename, 'w', encoding='utf-8') as file:
            file.write(note[0] + '|' + note[1] + '\n')


def del_note():
    if list_notes.selectedItems():
        i = 0
        text_note = list_notes.selectedItems()[0].text()
        for note in notes:
            if note[0] == text_note:
                os.remove('Zametki/' + note[1] + '.txt')
                notes.remove(note)
                list_notes.clear()
                for note in notes:
                    list_notes.addItem(note[0])
                print(notes)
            i += 1


def save_note():
    if list_notes.selectedItems():
        i = 0
        text_note = list_notes.selectedItems()[0].text()
        for note in notes:
            if note[0] == text_note:
                note[2] = text_field.toPlainText()
                filename = str(i) + '.txt'
                with open('Zametki/' + filename, 'w', encoding='utf-8') as file:
                    file.write(note[0] + '|' + str(i) + '\n')
                    file.write(note[2] + '\n')
                    for tag in note[3]:
                        file.write(tag + ' ')
            i += 1


def add_tag():
    if list_notes.selectedItems():
        i = 0
        name_note_ = list_notes.selectedItems()[0].text()
        tag_text_ = tag_text.text()
        if tag_text_:
            for note in notes:
                if note[0] == name_note_:
                    if tag_text_ not in note[3]:
                        note[3].append(tag_text_)
                        list_tags.addItem(tag_text_)
                        tag_text.clear()
                        filename = str(i) + '.txt'
                        with open('Zametki/' + filename, 'w', encoding='utf-8') as file:
                            file.write(note[0] + '|' + str(i) + '\n')
                            file.write(note[2] + '\n')
                            for tag in note[3]:
                                file.write(tag + ' ')
                i += 1


def del_tag():
    if list_notes.selectedItems():
        i = 0
        name_note_ = list_notes.selectedItems()[0].text()
        if list_tags.selectedItems():
            for note in notes:
                if note[0] == name_note_:
                    tag_text_ = list_tags.selectedItems()[0].text()
                    note[3].remove(tag_text_)
                    list_tags.clear()
                    list_tags.addItems(note[3])
                    filename = str(i) + '.txt'
                    with open('Zametki/' + filename, 'w', encoding='utf-8') as file:
                        file.write(note[0] + '|' + str(i) + '\n')
                        file.write(note[2] + '\n')
                        for tag in note[3]:
                            file.write(tag + ' ')
                i += 1


def search_tag():
    tag = tag_text.text()
    if button_search_note.text() == 'Искать заметки по тегу' and tag:
        notes_filtered = []
        for note in notes:
            if tag in note[3]:
                notes_filtered.append(note[0])
        button_search_note.setText('Сбросить поиск')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
    elif button_search_note.text() == 'Сбросить поиск':
        list_notes.clear()
        list_tags.clear()
        tag_text.clear()
        for note in notes:
            list_notes.addItem(note[0])
        button_search_note.setText('Искать заметки по тегу')


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
# list_notes.addItems(data)
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
button_add_to_note.clicked.connect(add_tag)
button_separate_to_note.clicked.connect(del_tag)
button_search_note.clicked.connect(search_tag)
for note in notes:
    list_notes.addItem(note[0])
main_win.setLayout(layout_h)
main_win.show()
app.exec_()
