from src.endpoints.base import Base


class Users(Base):
	endpoint = '/users'

	def login_user(self, options):
		return self.client.make_request('post', self.endpoint + '/login', options)

	def logout_user(self):
		return self.client.post(self.endpoint + '/logout')

	def create_user(self, options=None):
		return self.client.post(self.endpoint, options)

	def get_users(self, options=None):
		return self.client.get(	self.endpoint, options)

	def get_users_by_ids(self, options=None):
		return self.client.post(
			self.endpoint + '/ids',
			options
		)

	def get_users_by_usernames(self, options=None):
		return self.client.get(
			self.endpoint + '/usernames',
			options
		)

	def search_users(self, options=None):
		return self.client.get(
			self.endpoint + '/search',
			options
		)

	def autocomplete_users(self, options=None):
		return self.client.get(
			self.endpoint + '/autocomplete',
			options
		)

	def get_user(self, user_id, options=None):
		return self.client.get(
			self.endpoint + '/' + user_id,
			options
		)

	def update_user(self, user_id, options=None):
		return self.client.put(
			self.endpoint + '/' + user_id,
			options
		)

	def deactivate_user(self, user_id, options=None):
		return self.client.delete(
			self.endpoint + '/' + user_id,
			options
		)

	def patch_user(self, user_id, options=None):
		return self.client.put(
			self.endpoint + '/' + user_id + '/patch',
			options
		)

	def update_user_role(self, user_id, options=None):
		return self.client.put(
			self.endpoint + '/' + user_id + '/roles',
			options
		)

	def update_user_active_status(self, user_id, options=None):
		return self.client.put(
			self.endpoint + '/' + user_id + '/active',
			options
		)

	def get_user_profile_image(self, user_id, options=None):
		return self.client.get(
			self.endpoint + '/' + user_id + '/image',
			options
		)

	def set_user_profile_image(self, user_id, options=None):
		return self.client.post(
			self.endpoint + '/' + user_id + '/image',
			options
		)

	def get_user_by_username(self, username, options=None):
		return self.client.get(
			self.endpoint + '/username/' + username,
			options
		)

	def reset_password(self, options=None):
		return self.client.post(
			self.endpoint + '/password/reset',
			options
		)

	def update_user_mfa(self, user_id, options=None):
		return self.client.put(
			self.endpoint + '/' + user_id + '/mfa',
			options
		)

	def generate_mfa(self, user_id, options=None):
		return self.client.post(
			self.endpoint + '/' + user_id + '/mfa/generate',
			options
		)

	def check_mfa(self, options=None):
		return self.client.post(
			self.endpoint + '/mfa',
			options
		)

	def update_user_password(self, user_id, options=None):
		return self.client.put(
			self.endpoint + '/' + user_id + '/password',
			options
		)

	def send_password_reset_mail(self, options=None):
		return self.client.post(
			self.endpoint + '/password/reset/send',
			options
		)

	def get_user_by_email(self, email, options=None):
		return self.client.post(
			self.endpoint + '/email/' + email,
			options
		)

	def get_user_sessions(self, user_id, options=None):
		return self.client.get(
			self.endpoint + '/' + user_id + '/sessions',
			options
		)

	def revoke_user_session(self, user_id, options=None):
		return self.client.post(
			self.endpoint + '/' + user_id + '/sessions/revoke',
			options
		)

	def attach_mobile_device(self, options=None):
		return self.client.put(
			self.endpoint + '/sessions/device',
			options
		)

	def get_user_audits(self, user_id, options=None):
		return self.client.get(
			self.endpoint + '/' + user_id + '/audits',
			options
		)

	def verify_user_email(self, options=None):
		return self.client.post(
			self.endpoint + '/email/verify',
			options
		)

	def send_verification_mail(self, options=None):
		return self.client.post(
			self.endpoint + '/email/verify/send',
			options
		)

	def switch_login_method(self, options=None):
		return self.client.post(
			self.endpoint + '/login/switch',
			options
		)