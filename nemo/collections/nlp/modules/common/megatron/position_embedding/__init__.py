# coding=utf-8
# Copyright (c) 2023, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from nemo.collections.nlp.modules.common.megatron.position_embedding.alibi_relative_position_embedding import (
    ALiBiRelativePositionEmbedding,
)
from nemo.collections.nlp.modules.common.megatron.position_embedding.kerple_relative_position_embedding import (
    KERPLERelativePositionEmbedding,
)
from nemo.collections.nlp.modules.common.megatron.position_embedding.rotary_position_embedding import RotaryEmbedding
from nemo.collections.nlp.modules.common.megatron.position_embedding.sandwich_relative_position_embedding import (
    SandwitchRelativePositionEmbedding,
)
from nemo.collections.nlp.modules.common.megatron.position_embedding.t5_relative_position_embedding import (
    T5RelativePositionEmbedding,
)
from nemo.collections.nlp.modules.common.megatron.position_embedding.xpos_relative_position_embedding import (
    XPOSRelativePositionEmbedding,
)