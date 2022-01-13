# Copyright 2019 The Forte Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import abstractmethod
from typing import (
    List,
    Type,
    Union,
    Iterator,
    Dict,
    Tuple,
    Any,
)

from forte.common import EntryNotFoundError
from forte.data.ontology.core import EntryType

__all__ = ["BaseStore"]


class BaseStore:
    r"""The base class which will be used by :class:
    `~forte.data.data_store.DataStore`."""

    # pylint: disable=too-many-public-methods
    def __init__(self):
        r"""
        This is a base class for the efficient underlying data structure. A current
        implementation of `BaseStore` is `DataStore`.

        A `BaseStore` contains a piece of natural language text and a
        collection of NLP entries (annotations, links, and groups). The natural
        language text could be a document, paragraph or in any other granularity.
        """


    @abstractmethod
    def add_annotation_raw(self, type_id: int, begin: int, end: int) -> int:
        r"""This function adds an annotation entry with `begin` and `end` index
        to the sortedlist at index `type_id` of the array which records all
        sortedlists, return tid for the entry.

        Args:
            type_id (int): The index of Annotation sortedlist in the array.
            begin (int): begin index of the entry.
            end (int): end index of the entry.

        Returns:
            The tid of the entry.

        """
        raise NotImplementedError

    @abstractmethod
    def set_attr(self, tid: int, attr_name: str, attr_value):
        r"""This function locates the entry list with tid and sets its
        attribute `attr_name` with value `attr_value`.

        Args:
            tid (int): Unique id of the entry.
            attr_name (str): name of the attribute.
            attr_value: value of the attribute.

        """
 
        raise NotImplementedError

    @abstractmethod
    def get_attr(self, tid: int, attr_name: str):
        r"""This function locates the entry list with tid and gets the value
        of `attr_name` of this entry.

        Args:
            tid (int): Unique id of the entry.
            attr_name (str): name of the attribute.

        Returns:

        """
    
        raise NotImplementedError

    @abstractmethod
    def delete_entry(self, tid: int):
        r"""This function locates the entry list with tid and removes it
        from the data store. It removes the entry list from both entry_dict
        and the sortedlist of its type.

        Args:
            tid (int): Unique id of the entry.

        """
     

        raise NotImplementedError

    @abstractmethod
    def get_entry(self, tid: int) -> List:
        r"""Look up the entry_dict with key `tid`.

        Args:
            tid (int): Unique id of the entry.

        Returns:
            The entry which tid corresponds to.

        """
        raise NotImplementedError

    @abstractmethod
    def get(
        self, entry_type: Union[str, Type[EntryType]], **kwargs
    ) -> Iterator[List]:
        """
        Implementation of this method should provide to obtain the entries of
        type entry_type.

        Args:
            entry_type: The type of the entry to obtain.

        Returns:
            An iterator of the entries matching the provided arguments.

        """

        raise NotImplementedError

    @abstractmethod
    def next_entry(self, tid):
        r"""Get the next entry of the same type as the tid entry.

        Args:
            tid (int): Unique id of the entry.

        Returns:
            The next entry of the same type as the tid entry.

        """
      

        raise NotImplementedError

    @abstractmethod
    def prev_entry(self, tid):
        r"""Get the previous entry of the same type as the tid entry.

        Args:
            tid (int): Unique id of the entry.

        Returns:
            The previous entry of the same type as the tid entry.

        """

        raise NotImplementedError
