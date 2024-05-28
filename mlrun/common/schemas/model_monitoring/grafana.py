# Copyright 2023 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Optional, Union

from pydantic import BaseModel

import mlrun.common.types


class GrafanaColumnType(mlrun.common.types.StrEnum):
    NUMBER = "number"
    STRING = "string"


class GrafanaColumn(BaseModel):
    text: str
    type: str


class GrafanaNumberColumn(GrafanaColumn):
    type: str = GrafanaColumnType.NUMBER


class GrafanaStringColumn(GrafanaColumn):
    type: str = GrafanaColumnType.STRING


class GrafanaTable(BaseModel):
    columns: list[GrafanaColumn]
    rows: list[list[Optional[Union[float, int, str]]]] = []
    type: str = "table"

    def add_row(self, *args):
        self.rows.append(list(args))


class GrafanaDataPoint(BaseModel):
    value: float
    timestamp: int  # Unix timestamp in milliseconds


class GrafanaTimeSeriesTarget(BaseModel):
    target: str
    datapoints: list[tuple[float, int]] = []

    def add_data_point(self, data_point: GrafanaDataPoint):
        self.datapoints.append((data_point.value, data_point.timestamp))
