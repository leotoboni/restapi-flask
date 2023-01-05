APP = restapi

test:
	@flake8 . --exclude .ven

compose:
	@docker-compose build
	@docker-compose up
