"""fix_calendar_defaults

Revision ID: 2192f61f60d5
Revises: 1bbf7ca27d8b
Create Date: 2015-02-18 19:37:44.107084

"""

# revision identifiers, used by Alembic.
revision = '2192f61f60d5'
down_revision = '1bbf7ca27d8b'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


def upgrade():
    conn = op.get_bind()
    conn.execute(text("ALTER TABLE calendar MODIFY namespace_id int(11) NOT NULL;"))
    conn.execute(text("ALTER TABLE calendar MODIFY created_at DATETIME NOT NULL;"))
    conn.execute(text("ALTER TABLE calendar MODIFY uid varchar(767) DATETIME NOT NULL;"))
    conn.execute(text("ALTER TABLE account DROP CONSTRAINT `calendar_ibfk_2`"))
    conn.execute(text("ALTER TABLE account ADD CONSTRAINT `calendar_ibfk_2` FOREIGN KEY (`default_calendar_id`) REFERENCES `calendar` (`id`) ON DELETE CASCADE"))


def downgrade():
    conn = op.get_bind()
    conn.execute(text("ALTER TABLE calendar MODIFY namespace_id int(11);"))
    conn.execute(text("ALTER TABLE calendar MODIFY created_at DATETIME;"))
    conn.execute(text("ALTER TABLE calendar MODIFY uid varchar(767) DATETIME;"))
    conn.execute(text("ALTER TABLE account DROP CONSTRAINT `calendar_ibfk_2`"))
    conn.execute(text("ALTER TABLE account ADD CONSTRAINT `calendar_ibfk_2` FOREIGN KEY (`default_calendar_id`) REFERENCES `calendar` (`id`)"))
