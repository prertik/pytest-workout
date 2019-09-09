# -*- coding: utf-8 -*-
"""Top-level package for pytest-workout."""

from .api import (Task, TasksException, add, get, list_tasks, count, update,
                  delete, delete_all, unique_id, start_tasks_db, stop_tasks_db)

__author__ = """Pratik Karki"""
__email__ = 'predatoramigo@gmail.com'
__version__ = '0.0.1'
