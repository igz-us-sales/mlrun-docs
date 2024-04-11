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
#

"""adding table datastore_profiles

Revision ID: 6e0c9531edc7
Revises: 4acd9430b093
Create Date: 2023-06-30 13:44:34.141769

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "6e0c9531edc7"
down_revision = "4acd9430b093"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "datastore_profiles",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("type", sa.String(length=255), nullable=True),
        sa.Column("project", sa.String(length=255), nullable=True),
        sa.Column("body", sa.String(length=1024), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "project", name="_datastore_profiles_uc"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("datastore_profiles")
    # ### end Alembic commands ###
