from aiogram import types
from dispatcher import dp
from handlers.utils import get_patients, Stage, add_patient


DEFAULT = 'You can get a list of patients or add a new patient by selecting one of the commands in the menu'
WRONG_AGE = 'It seems that you entered not a number'
END_MESSAGE = 'Ok, now I will add this patient'
NAME = 'name'
AGE = 'age'
DESEASE = 'desease'
GET_MSG = 'Ok, catch it!\n'
ADD_MSG = "Ok, let's write it down!\n"
CANCEL_MSG = 'Adding new patient canceled'


stage = Stage.ANY_COMMAND_EXPECTED
new_patient = dict()


@dp.message_handler(commands=['get_all'])
async def get_patients_command(message: types.Message):
    global stage
    stage = Stage.ANY_COMMAND_EXPECTED
    patients = get_patients()
    await message.answer(GET_MSG + patients)


@dp.message_handler(commands=['add_new'])
async def add_patients_command(message: types.Message):

    global stage
    stage = Stage.NAME_EXPECTED
    await message.answer(ADD_MSG + stage.value)


@dp.message_handler(commands=['cancel'])
async def cancel_adding_command(message: types.Message):
    global stage
    stage = Stage.ANY_COMMAND_EXPECTED
    await message.answer(CANCEL_MSG)


@dp.message_handler()
async def handle_text(message: types.Message):
    global stage
    global new_patient
    answer = DEFAULT
    msg_text = message['text']
    if stage == Stage.ANY_COMMAND_EXPECTED:
        answer = DEFAULT
    elif stage == Stage.NAME_EXPECTED:
        new_patient[NAME] = msg_text
        stage = Stage.AGE_EXPECTED
        answer = stage.value
    elif stage == Stage.AGE_EXPECTED:
        if msg_text.isdigit():
            new_patient[AGE] = int(msg_text)
            stage = stage.DESEASE_EXPECTED
            answer = stage.value
        else:
            answer = WRONG_AGE
        answer = stage.value
    elif stage == Stage.DESEASE_EXPECTED:
        new_patient[DESEASE] = msg_text
        add_patient(new_patient)
        stage = Stage.ANY_COMMAND_EXPECTED
        answer = END_MESSAGE

    await message.answer(answer)