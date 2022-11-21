"""Initial migration.

Revision ID: 67be0a880342
Revises: 
Create Date: 2022-11-18 16:51:39.309508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67be0a880342'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('asset_transaction',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('src_wallet_id', sa.BigInteger(), nullable=True),
    sa.Column('src_asset_id', sa.BigInteger(), nullable=True),
    sa.Column('dest_wallet_id', sa.BigInteger(), nullable=True),
    sa.Column('dest_asset_id', sa.BigInteger(), nullable=True),
    sa.Column('amount', sa.Numeric(precision=16, scale=8), nullable=True),
    sa.Column('gas_fee', sa.Numeric(precision=16, scale=8), nullable=True),
    sa.Column('total', sa.Numeric(precision=16, scale=8), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assets',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('wallet_id', sa.BigInteger(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('symbol', sa.String(length=100), nullable=True),
    sa.Column('network', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=42), nullable=True),
    sa.Column('balance', sa.Numeric(precision=16, scale=8), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wallets',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallets')
    op.drop_table('assets')
    op.drop_table('asset_transaction')
    # ### end Alembic commands ###