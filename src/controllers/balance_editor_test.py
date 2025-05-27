from .balance_editor import BalanceEditor

class MockUserRepository:
    def edit_balance(self, user_id, new_balance) -> None:
     pass

def test_edit_balance():
    mock_repo = MockUserRepository()
    balance_editor = BalanceEditor(mock_repo)

    response = balance_editor.edit(user_id=1, new_balance=1000)

    assert response ["type"] == "User"
    assert response ["count"] == 1
    assert response ["new balance"] == 1000
