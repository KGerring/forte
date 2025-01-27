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

from typing import Dict, List, Tuple, Type, Union

import torch
import numpy as np

from forte.data.ontology.core import Entry
from forte.data.span import Span

__all__ = ["ReplaceOperationsType", "DataRequest", "MatrixLike"]

ReplaceOperationsType = List[Tuple[Span, str]]

DataRequest = Dict[Type[Entry], Union[Dict, List]]

MatrixLike = Union[torch.TensorType, np.ndarray, List]
