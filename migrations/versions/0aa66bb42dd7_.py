"""empty message

Revision ID: 0aa66bb42dd7
Revises: 
Create Date: 2025-02-28 11:29:15.186124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0aa66bb42dd7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('userID', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('userID'),
    sa.UniqueConstraint('userID')
    )
    op.create_table('expenses',
    sa.Column('expenseID', sa.Integer(), nullable=False),
    sa.Column('payerId', sa.Integer(), nullable=True),
    sa.Column('shared_between', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['payerId'], ['user.userID'], ),
    sa.PrimaryKeyConstraint('expenseID'),
    sa.UniqueConstraint('expenseID')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_userid', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(length=200), nullable=True),
    sa.Column('sent_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['from_userid'], ['user.userID'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('debts',
    sa.Column('debtID', sa.Integer(), nullable=False),
    sa.Column('expensesID', sa.Integer(), nullable=True),
    sa.Column('debtorID', sa.Integer(), nullable=True),
    sa.Column('amount_to_pay', sa.Integer(), nullable=False),
    sa.Column('is_paid', sa.Boolean(), nullable=False),
    sa.Column('payed_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['debtorID'], ['user.userID'], ),
    sa.ForeignKeyConstraint(['expensesID'], ['expenses.expenseID'], ),
    sa.PrimaryKeyConstraint('debtID'),
    sa.UniqueConstraint('debtID')
    )
    op.create_table('group',
    sa.Column('groupID', sa.Integer(), nullable=False),
    sa.Column('group_name', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('total_Amount', sa.Integer(), nullable=False),
    sa.Column('expenses', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['expenses'], ['expenses.expenseID'], ),
    sa.PrimaryKeyConstraint('groupID'),
    sa.UniqueConstraint('groupID')
    )
    op.create_table('group_payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('receiverID', sa.Integer(), nullable=False),
    sa.Column('payerID', sa.Integer(), nullable=False),
    sa.Column('groupID', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('payed_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['groupID'], ['group.groupID'], ),
    sa.ForeignKeyConstraint(['payerID'], ['user.userID'], ),
    sa.ForeignKeyConstraint(['receiverID'], ['user.userID'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('group_to_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userID', sa.Integer(), nullable=True),
    sa.Column('groupId', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['groupId'], ['group.groupID'], ),
    sa.ForeignKeyConstraint(['userID'], ['user.userID'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('objectives',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('groupID', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('targetAmount', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('is_completed', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['groupID'], ['group.groupID'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('debtID', sa.Integer(), nullable=True),
    sa.Column('payerID', sa.Integer(), nullable=True),
    sa.Column('receiverID', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('payed_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['debtID'], ['debts.debtID'], ),
    sa.ForeignKeyConstraint(['payerID'], ['user.userID'], ),
    sa.ForeignKeyConstraint(['receiverID'], ['user.userID'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('objetive_contributions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('objectiveID', sa.Integer(), nullable=True),
    sa.Column('userID', sa.Integer(), nullable=True),
    sa.Column('amount_contributed', sa.Integer(), nullable=False),
    sa.Column('contributed_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['objectiveID'], ['objectives.id'], ),
    sa.ForeignKeyConstraint(['userID'], ['user.userID'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('objetive_contributions')
    op.drop_table('payments')
    op.drop_table('objectives')
    op.drop_table('group_to_user')
    op.drop_table('group_payments')
    op.drop_table('group')
    op.drop_table('debts')
    op.drop_table('messages')
    op.drop_table('expenses')
    op.drop_table('user')
    # ### end Alembic commands ###
