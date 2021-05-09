import multiprocessing as mp
from typing import Callable, Any


class TaskStatus:
    def __init__(self, pid: int, is_alive=False):
        self.pid = pid
        self.is_running = is_alive


class MyPool:

    def __init__(self, max_size: int):
        """класс, реализующий пул процессов для выполнения задач

        :param max_size: максимальный размер пула процессов
        """
        self._tasks: dict[str, Callable] = {}
        self._processes: dict[str, mp.Process] = {}
        self._max_size: int = max_size

    def add_task(self, task_name: str, task: Callable, *args: list[Any], **kwargs: dict[Any, Any]) -> bool:
        """запускает задачу на выполнение.

        Имя задачи должно быть уникальным в пуле.

        :param task_name: имя новой задачи
        :param task: задача
        :param args: параметры задачи
        :param kwargs: параметры задачи
        :return:  True - если задача была успешно добавлена, иначе - False
        """
        # TODO: Реализовать метод.
        #  Если число запущенных процессов < размера пула - запускает новый процесс с переданной задачей.
        #  Если число запущенных процессов == размеру пула - задача заносится в tasks

    def _run(self):
        """
        Рабочий цикл пула
        :return:
        """
        # TODO: реализовать метод.
        #  Цикл предназначен для получения ожидающих задач из tasks и запуска процессов по мере их завершения

    def remove_task(self, task_name: str) -> bool:
        """ уничтожает задачу с именем task_name.

        :param task_name: имя уничтожаемой задачи
        :return: True - если задача была успешно удалена, иначе - False
        """

        # TODO: реализовать метод.
        #  Удаляет задачу из tasks, если она еще не была запущена.
        #  Уничтожает процесс задачи, если удаляемая задача уже была запущена

    def get_task_info(self, task_name: str) -> TaskStatus:
        """возвращает информацию о процессе выполнения задачи

        :param task_name: имя задачи
        :return: объект TaskStatus, хранящий в себе параметры задачи, а именно:
            статус задачи - is_running: True - если задача выполняется, иначе False.
            идентификатор выполяющего процесса - pid: числовой идентификатор процесса - если задача выполняется,
                иначе None
        """
        # TODO: реализовать метод

    def wait_all(self):
        """ожидает завершения всех текущих задач.

        :return:
        """
        # TODO: реализовать метод

    def wait_task(self, task_name: str):
        """ожидает завершения задачи под именем task_name.

        :param task_name: имя ожиадемой задачи
        :return:
        """
        # TODO: реализовать функцию
